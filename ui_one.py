import tkinter as tk

def salvar_nome_endereco():
    nome = entry_nome.get()
    endereco = entry_endereco.get()
    if nome:
        with open("nomes_endereco.txt", "a") as arquivo:
            arquivo.write("Nome:" + nome + '\n' + "Endereço:" + endereco + '\n')

        label_status.config(text=f'Nome "{nome}" e o endereço "{endereco}" foram salvos com sucesso!', fg="green")
    else:
        label_status.config(text="Digite um nome e o endereço.", fg="red")

root = tk.Tk()
root.title("Nomes e Endereços")
root.geometry("500x250")

label_instrucao = tk.Label(root, text="Digite um nome:")
label_instrucao.pack(pady=10)

entry_nome = tk.Entry(root)
entry_nome.pack(pady=5)

label_instrucao = tk.Label(root, text="Digite o endereço:")
label_instrucao.pack(pady=10)

entry_endereco = tk.Entry(root)
entry_endereco.pack(pady=5)

botao_salvar = tk.Button(root, text="Salvar", command=salvar_nome_endereco)
botao_salvar.pack(pady=10)

label_status = tk.Label(root, text="")
label_status.pack(pady=5)
root.mainloop()
