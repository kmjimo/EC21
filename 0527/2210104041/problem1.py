# -*- coding: utf-8 -*-

# 素数リストの作成
def is_prime(maxnum):
    prime_list = []
    for i in range(2,maxnum):
        flag = 0
        for j in range(2,i//2+1):
            if (i%j==0):
                flag = 1
                break
        if flag == 0:
                prime_list.append(i)
    return prime_list

# 部分和問題
def find_max_dp(num_list,limit):
    list_len = len(num_list)

    # DPテーブル
    dp_table = [[0 for i in range(limit + 1)] for i in range(list_len + 1)]

    # 復元用テーブル
    prev = [[0 for i in range(limit + 1)] for i in range(list_len + 1)]

    # DPループ
    for i in range(list_len):
        for j in range(limit + 1):
            if num_list[i] <= j:
                dp_table[i+1][j] = max(dp_table[i][j - num_list[i]] + num_list[i],dp_table[i][j])
                prev[i+1][j] = j - num_list[i]
            else:
                dp_table[i+1][j] = dp_table[i][j]
                prev[i+1][j] = j

    # 復元
    ans = []
    for i in reversed(range(list_len)):
        if prev[i][limit] == limit - num_list[i-1]:
            ans.append(num_list[i-1])
        limit = prev[i][limit]

    return ans


if __name__ == '__main__':
    s = is_prime(100)
    Sa = find_max_dp(s,sum(s)//2)
    Sb = list(set(s) ^ set(Sa))
    print(Sa)
    print(sum(Sa))
    print(Sb)
    print(sum(Sb))
