# Credit card validator using the Luhn algorithm
def is_valid_credit_card(card_num):
    card_num = str(card_num)
    num_digits = len(card_num)
    odd_sum = sum(int(card_num[i]) for i in range(num_digits - 1, -1, -2))
    even_sum = sum(sum(divmod(int(card_num[i]) * 2, 10)) for i in range(num_digits - 2, -1, -2))
    total_sum = odd_sum + even_sum
    return total_sum % 10 == 0

# Example usage
card_num = "4556737586899855"
is_valid = is_valid_credit_card(card_num)
print(is_valid)  # Output: True
