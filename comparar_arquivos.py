import json

qtd = 0

pasta = 'jsons/connections/followers_and_following/'

with open(pasta + 'followers_1.json', encoding='utf-8') as f:
    seguidores_raw = json.load(f)

with open(pasta + 'following.json', encoding='utf-8') as f:
    seguindo_raw = json.load(f)

if isinstance(seguidores_raw, dict):
    seguidores_raw = seguidores_raw.get("string_list_data", seguidores_raw)

if isinstance(seguindo_raw, dict):
    seguindo_raw = seguindo_raw.get("relationships_following", seguindo_raw)

# --- Extrair usernames (campo "title") ---
seguidores = sorted({
    item["string_list_data"][0]["value"] # entra no string_list_data, vai no indice 0 (so tem um campo com informacoes), dai escolhe a informacao que quer
    for item in seguidores_raw
    })

seguindo = sorted({
    item["title"] 
    for item in seguindo_raw}
    )

sigo_e_segue = []
segue_e_nao_sigo = []      # me seguem, mas eu não sigo de volta
sigo_e_nao_me_segue = []   # eu sigo, mas não me seguem de volta

for nome in seguidores:
    if nome in seguindo:
        sigo_e_segue.append(nome)
    else:
        segue_e_nao_sigo.append(nome)

for nome in seguindo:
    if nome not in seguidores:
        sigo_e_nao_me_segue.append(nome)

sigo_e_segue_num = len(sigo_e_segue)
segue_e_nao_sigo_num = len(segue_e_nao_sigo)
sigo_e_nao_segue_num = len(sigo_e_nao_me_segue)


op = 0
while op != 4:
    print(" 1: seguidores que te seguem e voce segue de volta\n 2: seguidores que te seguem e voce nao segue de volta\n 3: seguidores que te seguem e vc nao segue de volta")
    op = int(input("digite a opcao que quer ver: "))
    
    match op:
        case 1:
            print(f"total de seguidores que te seguem: {sigo_e_segue_num}")
            for nomes in sigo_e_segue:
                print(f"seguidor:", nomes)
        case 2:
            print(f"total de seguidores que te seguem e voce nao segue de volta: {sigo_e_nao_segue_num}")
            for nomes in sigo_e_nao_me_segue:
                print(f"seguidor:", nomes)
        case 3:
            print(f"total de seguidores que te seguem e vc nao segue de volta: {segue_e_nao_sigo_num}")
            for nomes in segue_e_nao_sigo:
                print(f"seguidor:", nomes)
        case 4:
            print("saindo...")