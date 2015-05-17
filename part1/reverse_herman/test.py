from reverse_string import reverse


print(reverse("tset") == "test")             # True
print(reverse("olleh") == "hello")           # True
print(reverse("nekcihc") == "chicken")       # True
print(reverse("neckihc") == "notchicken")    # False
print(reverse("abcdefghijklmnopqrstuvwxyz") ==
      "zyxwvutsrqponmlkjihgfedcba")          # True
