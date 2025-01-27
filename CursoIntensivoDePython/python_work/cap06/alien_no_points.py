print('\nPrograma-01')
alien_0 = {'color': 'green', 'speed': 'slow'}
# Erro comentado
# print(alien_0['points'])
# Resultado:
#   Traceback (most recent call last):
#     File "alien_no_points.py", line 2, in <module>
#       print(alien_0['points'])
#             ~~~~~~~^^^^^^^^^^
#   KeyError: 'points'

print('\nPrograma-02')
alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No points value assigned.')
print(point_value)
