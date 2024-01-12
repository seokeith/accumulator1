import streamlit as st

def fractional_odds_to_decimal(fraction):
    num, denom = map(int, fraction.split('/'))
    return num / denom + 1

def calculate_payout(unit_stake, odds, each_way, each_way_fraction):
    total_payout = 0
    for odd in odds:
        decimal_odd = fractional_odds_to_decimal(odd)
        payout = unit_stake * decimal_odd
        total_payout += payout
        if each_way:
            num, denom = map(int, each_way_fraction.split('/'))
            total_payout += unit_stake * (decimal_odd - 1) * num / denom
    return total_payout

# App title
st.title("Accumulator Bet Payout Calculator")

# User inputs
unit_stake = st.number_input("Enter your unit stake", min_value=0.0, value=10.0)
number_of_bets = st.slider("Select number of bets", 1, 10, 3)
each_way = st.checkbox("Each Way Bet")
each_way_fraction = st.selectbox("Select Each Way Fraction", ["1/1", "1/2", "1/3", "1/4", "1/5", "1/6", "1/7", "1/8"], index=3) if each_way else "1/1"

if each_way:
    unit_stake *= 2  # Double the stake if each way is selected

odds = []
for i in range(number_of_bets):
    odd = st.text_input(f"Enter fractional odds for bet {i+1} (e.g., 2/1)", value="2/1", key=f"odds_{i}")
    odds.append(odd)

if st.button("Calculate Payout"):
    payout = calculate_payout(unit_stake, odds, each_way, each_way_fraction)
    st.success(f"Your total payout is {payout:.2f}")

