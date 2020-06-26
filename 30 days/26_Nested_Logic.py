returned_date = [int (a) for a in input().split(' ', 3)]
due_date = [int (b) for b in input().split(' ', 3)]
if returned_date[2] == due_date[2] and returned_date[1] == due_date[1]:
    if returned_date[0] < due_date[0]:
        print("0")
    else:
        fine = 15*(returned_date[0] - due_date[0])
        print(fine)

elif returned_date[2] == due_date[2]:
    if returned_date[1] < due_date[1]:
        print("0")
    else:
        fine = 500*(returned_date[1] - due_date[1])
        print(fine)

else:
    if returned_date[2] > due_date[2]:
        print('10000')
    else:
        print('0')