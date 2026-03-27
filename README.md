# Sistema de Revisão por Repetição Espaçada

O sistema é baseado no algoritmo de repetição espaçada, que calcula automaticamente a data ideal para você revisar cada tópico com base no seu histórico de revisões. Quanto mais vezes você revisar um tópico com sucesso, maior será o intervalo até a próxima revisão. Tópicos que você tem mais dificuldade aparecem com mais frequência.

A tela principal exibe todos os tópicos que precisam ser revisados no dia atual em destaque, para que você saiba exatamente por onde começar.

---

## Funcionalidades

- Cadastro de matérias, assuntos, tópicos e subtópicos
- Cálculo automático da próxima data de revisão com base no algoritmo de repetição espaçada
- Destaque para os tópicos que devem ser revisados no dia atual
- Persistência de todos os dados em banco de dados local

---

## Tecnologias utilizadas

- **Python** — linguagem principal do projeto
- **SQLite** — banco de dados local 
- **Tkinter** — interface gráfica

---

## Estrutura do banco de dados

```
materia
├── id (PK)
└── nome

assunto
├── id (PK)
├── nome
└── id_materia (FK → materia)

topico
├── id (PK)
├── nome
└── id_assunto (FK → assunto)

subtopico
├── id (PK)
├── nome
├── id_topico (FK → topico)
├── data_estudo
├── data_revisao
├── ultima_revisao
└── numero_revisoes
```

---

## Como executar

Clone o repositório:

```bash
git clone https://github.com/yan-dhsk/Revisao-Espacada
```

Acesse a pasta do projeto:

```bash
cd Revisao-Espacada
```

Execute o programa:

```bash
python main.py
```

Nenhuma dependência externa precisa ser instalada. O projeto utiliza apenas bibliotecas nativas do Python.

---

## Autor

Desenvolvido por [Yan Neves](https://github.com/yan-dhsk)
