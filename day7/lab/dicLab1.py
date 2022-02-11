color={'red':(255,0,0),'blue':(0,0,255)
,'yellow':(255,255,0),'orange':(255,165,0)
,'white':(255,255,255),'black':(0,0,0)
,'violet':(238,130,238),'pink':(255,192,203)
,'lime':(0,255,0)}

col=input("칼라명을 영문으로 입력하세요 :")
if col in color:
    print(f'{col} 칼라의 RGB 값은 {color[col]} 입니다')
else:
    print(f'{col} 칼라의 RGB 값을 찾을 수 없습니다')