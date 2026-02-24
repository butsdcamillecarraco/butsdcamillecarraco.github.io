def hex_to_rgb(h):
    h = h.lstrip('#')
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def srgb_lin(c):
    c = c / 255.0
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4

def luminance(hexcol):
    r, g, b = hex_to_rgb(hexcol)
    R = srgb_lin(r)
    G = srgb_lin(g)
    B = srgb_lin(b)
    return 0.2126 * R + 0.7152 * G + 0.0722 * B

def contrast(a, b):
    La = luminance(a)
    Lb = luminance(b)
    L1 = max(La, Lb)
    L2 = min(La, Lb)
    return (L1 + 0.05) / (L2 + 0.05)

colors = {
    'bg': '#f4f6f8',
    'card': '#ffffff',
    'muted': '#263834',
    'muted-secondary': '#556a66',
    'accent': '#2F6B86',
    'accent-deep': '#1F4B56',
    'accent-soft': '#e9eef1'
}

pairs = [
    ('texte / fond', 'muted', 'bg'),
    ('texte secondaire / fond', 'muted-secondary', 'bg'),
    ('accent / fond', 'accent', 'bg'),
    ('accent-deep / card', 'accent-deep', 'card'),
    ('button text / button bg', 'card', 'accent-deep'),
    ('card border / card', 'accent-soft', 'card'),
]

print('Contraste (rapport) — valeurs -> objectif AA 4.5 (texte normal)')
for label, a, b in pairs:
    r = contrast(colors[a], colors[b])
    print(f"{label:30}: {colors[a]} on {colors[b]} -> {r:.2f}")

# Suggest simple guidance
print('\nGuidance:')
print('- >= 4.5 : bon pour texte normal (AA)')
print('- >= 3.0 : bon pour grand texte (18pt+)')
print('- < 3.0 : envisager éclaircir/sombrer')
