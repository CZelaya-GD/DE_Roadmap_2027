import pandas as pd
import random
import time

# Create sample data
random.seed(42)

df = pd.DataFrame({
    "price": [random.uniform(10, 100) for _ in range(100_000)],
    "quantity": [random.randint(1, 10) for _ in range(100_000)],
})

# FOR-LOOP VERSION
start = time.perf_counter()

totals = []

for _, row in df.iterrows():
    total = row["price"] * row["quantity"]

    if total >= 300:
        total *= 0.90

    totals.append(total)

df["final_total"] = totals

loop_time = time.perf_counter() - start

print(df.head())
print(f"For-loop time: {loop_time:.6f} seconds")

# VECTORIZED VERSION
start = time.perf_counter()

# Valid approach 
# df["final_total_vectorized"] = df["price"] * df["quantity"] 
# df.loc[df["final_total_vectorized"] >=300, 
#           "final_total_vectorized"] *= 0.90

# Cleaner vectorized approach
totals = df["price"] * df["quantity"]

totals.loc[totals >=300] *= 0.90

df["final_total_vectorized"] = totals

vectorized_time = time.perf_counter() - start

print(df.head())
print(f"Vectorized time: {vectorized_time:.6f} seconds")
print(
    (df["final_total"] == df["final_total_vectorized"]).all()
)