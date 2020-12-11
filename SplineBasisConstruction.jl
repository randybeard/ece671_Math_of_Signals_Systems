import Plots
import LinearAlgebra

# p : Polynomial degree
# i : Basis function index.  Valid input is 0 to p.
function bernstein( p::Integer, i::Integer )
    if i > p || i < 0
        return xi -> 0
    end
    return xi -> binomial( p, i ) * ( 1 - xi ) ^ ( p - i ) * xi ^ i
end

# p : Polynomial degree
# i : Basis function index.  Valid input is 0 to p.
# n : Derivative order
function dBdxi( p::Integer, i::Integer, n::Integer )
    if n == 0
        return bernstein( p, i )
    end

    if p < 0
        return xi -> 0
    end

    return xi -> p*( dBdxi( p - 1, i - 1, n - 1 )( xi ) - dBdxi( p - 1, i, n - 1 )( xi ) )
end

################## Mesh Functionality ###################

struct Mesh
    degrees
    smoothnesses
end

struct LocalFunc
    elem
    idx
end

function numLocalFunctions( mesh::Mesh )
    return sum( [ p + 1 for p in mesh.degrees ] )
end

function numContinuityConstraints( mesh::Mesh )
    return sum( [ k + 1 for k in mesh.smoothnesses ] )
end

function buildUniformMesh( n_elems::Integer, degree::Integer, smoothness::Integer )
    degrees = [ degree for i in 1:n_elems ]
    smoothnesses = [ smoothness for i in 2:n_elems ]
    return Mesh( degrees, smoothnesses )
end

# Local Bernstein indexing to global Bernstein indexing
function localToGlobal( mesh::Mesh, localfunc::LocalFunc )
    return ( localfunc.elem > 1 ? sum( [ mesh.degrees[ e ] + 1 for e in 1:localfunc.elem-1 ] ) : 0 ) + localfunc.idx + 1
end

function meshLocalFuncs( mesh::Mesh )
    return [ ( [ [ LocalFunc( elem, i ) for i in 0:mesh.degrees[ elem ] ] for elem in 1:length( mesh.degrees ) ]... )... ]
end


##################### Plotting functionality #############

function plotLocalBases!( plt, mesh::Mesh )
    for elem = 1:length( mesh.degrees )
        p = mesh.degrees[ elem ]
        Plots.plot!( plt, [ xi -> bernstein( p, i )( xi - elem + 1 ) for i in 0:p ], elem-1:0.01:(elem) )
    end
    plt
end

function plotSplineBasis!( plt, mesh::Mesh, coeffs )
    function splineFunction( mesh::Mesh, coeffs )
        return function ( elem, xi )
            p = mesh.degrees[ elem ]
            elem_coeffs = coeffs[ localToGlobal( mesh, LocalFunc( elem, 0 ) ):localToGlobal( mesh, LocalFunc( elem, p ) ) ];
            return sum( [ elem_coeffs[i+1]*bernstein( p, i )( xi ) for i in 0:p ] )
        end
    end

    for elem = 1:length( mesh.degrees )
        Plots.plot!(
		                plt,
				            [ xi -> splineFunction( mesh, coeffs[:,i] )( elem, xi - elem + 1 ) for i in 1:size( coeffs, 2 ) ],
					                elem-1:0.01:elem )
    end
end


function buildS( mesh::Mesh )
    S = zeros( numContinuityConstraints( mesh ), numLocalFunctions( mesh ) );
    constraint_index = 1;
    for i in 1:length( mesh.smoothnesses )
        for k in 0:mesh.smoothnesses[i]
            for lf_ii in 0:mesh.degrees[i]
                S[ constraint_index, localToGlobal( mesh, LocalFunc( i, lf_ii ) ) ] =
                        dBdxi( mesh.degrees[i], lf_ii, k )( 1.0 )
            end

            for lf_ii in 0:mesh.degrees[i+1]
                S[ constraint_index, localToGlobal( mesh, LocalFunc( i+1, lf_ii ) ) ] =
                        -dBdxi( mesh.degrees[i+1], lf_ii, k )( 0.0 )
            end
            constraint_index += 1
        end
    end
    return S
end;
