kasse = {2: 10, 1: 10, 0.50: 10, 0.20: 10, 0.10: 10, 0.05: 10}
einwurf = {2: 0, 1: 1, 0.50: 1, 0.20: 2, 0.10: 0, 0.05: 0}
rückgeld = {2: 0, 1: 0, 0.50: 0, 0.20: 0, 0.10: 0, 0.05: 0}
eingeworfen = 0

for münze in einwurf:
    kasse[münze] += einwurf[münze]
    eingeworfen += münze * einwurf[münze]
if eingeworfen < 2.50:
    print("Münzen einwerfen: {:.2f}" .format(2.50 - eingeworfen))
else:
    print("Getränk auswählen")
    if eingeworfen > 2.50:
        print("Rückgeld: {:.2f}" .format(eingeworfen - 2.50))

        zurück = round(eingeworfen - 2.50, 2)

        for i in kasse:
            rückgeld[i] = int(zurück // i)
            zurück -= rückgeld[i] * i
            kasse[i] -= rückgeld[i]
print(rückgeld)
print(kasse)