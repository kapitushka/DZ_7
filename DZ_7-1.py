import winsound

s = "In a distant, but not so unrealistic, future \
where mankind has abandoned earth because it has \
become covered with trash from products sold by \
the powerful multi-national Buy N Large corporation, \
WALLE, a garbage collecting robot has been left to \
clean up the mess. Mesmerized with trinkets of Earth's \
history and show tunes, WALLE is alone on Earth except \
for a sprightly pet cockroach. One day, EVE, a sleek \
(and dangerous) reconnaissance robot, is sent to Earth to \
find proof that life is once again sustainable."
# Step 1
print(f"Длина строки: {len(s)}")

# Step 2
print (s.lower())

# Step 3
print(s.replace('WALLE', 'WALL-E' ))

# Step 4
print("В тексте слово Earth было использовано ", s.count("Earth"))

winsound.Beep(5000, 500)
