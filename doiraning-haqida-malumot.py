"""Doirani radiusi orqali uning diamtri, perimetr va yuzasini aniqlovchi dastur
Tuzuvchi: Tuychiev Muxtorjon
Sana: 31.08.2022"""
def doira_info(r):
    
    PI=3.14
    radiusi=r
    diametri=r*2
    perimetri=2*PI*r
    yuzasi=PI*(r**2)
    
    info={
        'radius':radiusi,
        'diametr':diametri,
        'perimetr':perimetri,
        'yuza':yuzasi
        }
    return info
r=float(input(f"Doiraning radiusini kiriting: "))
info=doira_info(r)
print(f"Radiusi {r} bo`lgan doira haqida ma`lumotlar:"
      f"\nRadiusi: {info['radius']}"
      f"\nDiametri: {info['diametr']}"
      f"\nPerimetri: {info['perimetr']}"
      f"\nYuzasi: {info['yuza']}")
