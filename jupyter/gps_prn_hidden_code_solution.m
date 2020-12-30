clear, clc, close all;


%% Part A
load prn_codes.mat %load prn codes generated in python

prn(prn(:,:) == 0) = -1; %prn codes are 1s and 0s, need to change to 1s and -1s

%calculate the dot product between each code
ortho = zeros(32,32);
for i = 1:32
    for j = 1:32
        ortho(i,j) = prn(i,:)*prn(j,:).'/(norm(prn(i,:))*norm(prn(j,:)));
    end
end
%the dot product between orthogonal vectors is 0

%% Part B

load gps_prn_hidden_code.mat

%% solve the first word
solve1 = zeros(3,8);
for i = 1:3
    for j = 1:8
        starti = 1+(1023*(j-1))+(1023*8*(i-1));
        endi = 1023+(1023*(j-1))+(1023*8*(i-1));
        solve1(i,j) = round(code(starti:endi)*prn(1,:).'/1023);
    end
end
solve1(solve1(:,:) == -1) = 0;

hiddenword1 = char(bin2dec(num2str(solve1(:,:)))).';

%% solve the second word
solve2 = zeros(3,8);
for i = 1:3
    for j = 1:8
        starti = 1+(1023*(j-1))+(1023*8*(i-1));
        endi = 1023+(1023*(j-1))+(1023*8*(i-1));
        solve2(i,j) = round(code(starti:endi)*prn(2,:).'/1023);
    end
end
solve2(solve2(:,:) == -1) = 0;

hiddenword2 = char(bin2dec(num2str(solve2(:,:)))).';

%% solve the third word
solve3 = zeros(3,8);
for i = 1:3
    for j = 1:8
        starti = 1+(1023*(j-1))+(1023*8*(i-1));
        endi = 1023+(1023*(j-1))+(1023*8*(i-1));
        solve3(i,j) = round(code(starti:endi)*prn(3,:).'/1023);
    end
end
solve3(solve3(:,:) == -1) = 0;

hiddenword3 = char(bin2dec(num2str(solve3(:,:)))).';

%% solve the fourth word
solve4 = zeros(3,8);
for i = 1:3
    for j = 1:8
        starti = 1+(1023*(j-1))+(1023*8*(i-1));
        endi = 1023+(1023*(j-1))+(1023*8*(i-1));
        solve4(i,j) = round(code(starti:endi)*prn(4,:).'/1023);
    end
end
solve4(solve4(:,:) == -1) = 0;

hiddenword4 = char(bin2dec(num2str(solve4(:,:)))).';
