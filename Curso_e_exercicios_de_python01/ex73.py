print('Tabela Brasileirão')
times = 'São Paulo','Atlético-MG','Flamengo','Internacional', 'Grêmio', 'Palmeiras','Fluminense','Santos', 'Corinthians','Ceará','Athletico-PR','Atlético-GO','Bragantino','Fortaleza','Sport','Bahia','Vasco','Goiás','Botafogo','Coritiba'
print(times[:6])
print(times[16:])
print(sorted(times))
print(f'O Ceará esta na {1 + (times.index("Ceará"))} posição')