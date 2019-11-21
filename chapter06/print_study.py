print("test", "test1", sep=" ")
print("%s %d" % ('test', 10))

a = 0.123456789
print("{0:.2f}, {0:.5f}".format(a))

print("2자리 {0:2d}, 0을 포함한 2자리 {0:02d},  \n왼쪽정렬 :{0:<5d}, 오른쪽 정렬 {0:>5d}".format(3))
print("세자리 구분기호 {0:,d}\n백분율 표시 {1:.1%}".format(1234567, 0.5))
print("16진수 : {0:#x} 8진수 : {0:#o}, 2진수 : {0:#b}".format(32), end="\t")
print("16진수 : {0:x} 8진수 : {0:o}, 2진수 : {0:b}".format(32))