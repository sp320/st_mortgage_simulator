import streamlit as st


def calc_payment(borrow: float, rate: float, years: float) -> float:
    monthly_rate = rate / 100 / 12
    monthly_payment = (borrow * monthly_rate) / (
        1 - (1 + monthly_rate) ** (-years * 12)
    )
    return monthly_payment


def calc_borrow(rate: float, years: float, monthly_payment: float) -> float:
    monthly_rate = rate / 100 / 12
    borrow = (monthly_payment / monthly_rate) * (
        1 - (1 + monthly_rate) ** (-years * 12)
    )
    return borrow


st.title("Loan Calculator")
