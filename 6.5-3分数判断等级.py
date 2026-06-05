score = int(input('请输入考试分数：'))
if score >= 90:
    print(f'你的分数是：{score},等级：优秀')
elif score >=80:
    print(f'你的分数是：{score},等级：良好')
elif score >=60:
    print(f'你的分数是：{score},等级：及格')
else:
    print(f'你的分数是：{score},等级：不及格')