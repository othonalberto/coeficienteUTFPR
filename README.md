# coeficiente-UTFPR

## Simule o coeficiente com futuras notas

Arquivo exemplo: `` document.xls ``

Extensões suportadas: xls, xlsx e ods. 

Graças a: [Rows](https://github.com/turicas/rows)

---

Para rodar: (recomendo fortemente o uso de virtualenv)
```
pip3 install -r requirements.txt

python3 ./src/main.py

```

## Como utilizar
    # para ler um documento
    notas = document.Document('nomeArquivo.xls')

    # calcular o coeficiente
    coef = gpa.Gpa()
    coef.set_gpa(notas) # quando um documento é importado é necessário passá-lo para a função

    # adicionar notas
    novaNota = subject.Subject(10, 90)

    # gerar coeficiente atualizado
    coef.insert_subject(novaNota)
    coef.set_gpa()

    # printar coeficiente
    print(coef.get_gpa())

### ATENÇÃO! 

Este projeto foi criado por mim por três motivos:
 
1. Aprender Python;
2. diversão;
3. ser algo útil para mim.

Portanto, **não há** qualquer ligação com a instituição UTFPR. Qualquer
reclamação/sugestão deve ser direcionada a mim.
