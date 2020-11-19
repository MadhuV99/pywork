# user.py
user_0 = {
'username': 'efermi',
'first': 'enrico',
'last': 'fermi',
}
print(user_0)
print(user_0.items())
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")