import matplotlib.pyplot as plt

grafico1 = [1, 3, 5, 7, 9]
valores1 = [2, 3, 7, 1, 2]
ponto = [200, 320, 150, 90, 210]

titulo = 'Scatterplot: Gráfico de dispersão'
eixox = 'Eixo X'
eixoy = 'Eixo Y'

#legendas
plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(grafico1, valores1, label='Meus Pontos', color='#0000FF', marker='o', s=ponto) #plot grafico de dispersão
plt.plot(grafico1, valores1, color='k', linestyle=':')
plt.legend()
#plt.show()
plt.savefig('Figura.png', dpi=300)


'''
Markers

character	description
'.'	point marker
','	pixel marker
'o'	circle marker
'v'	triangle_down marker
'^'	triangle_up marker
'<'	triangle_left marker
'>'	triangle_right marker
'1'	tri_down marker
'2'	tri_up marker
'3'	tri_left marker
'4'	tri_right marker
's'	square marker
'p'	pentagon marker
'*'	star marker
'h'	hexagon1 marker
'H'	hexagon2 marker
'+'	plus marker
'x'	x marker
'D'	diamond marker
'd'	thin_diamond marker
'|'	vline marker
'_'	hline marker
Line Styles

character	description
'-'	solid line style
'--'	dashed line style
'-.'	dash-dot line style
':'	dotted line style
Example format strings:

'b'    # blue markers with default shape
'or'   # red circles
'-g'   # green solid line
'--'   # dashed line with default color
'^k:'  # black triangle_up markers connected by a dotted line
Colors

The supported color abbreviations are the single letter codes

character	color
'b'	blue
'g'	green
'r'	red
'c'	cyan
'm'	magenta
'y'	yellow
'k'	black
'w'	white   
'''