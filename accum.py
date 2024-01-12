import streamlit as st

def calculate_payout(initial_bet, odds, multipliers):
    payout = initial_bet
    for i in range(len(odds)):
        payout *= odds[i] * (multipliers[i] if i < len(multipliers) else 1)
    return payout

# App title
st.title("Accumulator Bet Payout Calculator")

# User inputs
initial_bet = st.number_input("Enter your initial bet", min_value=0.0, value=10.0)
number_of_bets = st.slider("Select number of bets", 1, 10, 3)

odds = []
multipliers = []
for i in range(number_of_bets):
    odd = st.number_input(f"Enter odds for bet {i+1}", min_value=1.0, value=2.0, key=f"odds_{i}")
    odds.append(odd)
    if i < number_of_bets - 1: # Assuming multipliers are for transitions between bets
        multiplier = st.number_input(f"Enter multiplier after bet {i+1}", min_value=1.0, value=1.0, key=f"multiplier_{i}")
        multipliers.append(multiplier)

if st.button("Calculate Payout"):
    payout = calculate_payout(initial_bet, odds, multipliers)
    st.success(f"Your total payout is {payout:.2f}")

