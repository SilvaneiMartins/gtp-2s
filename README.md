<h1 align="center">
    GPT-2s
</h1>

<h4 align="center">
    GPT-2s é uma reimplementação do GPT-2 em C11, com passagem para frente e para trás.
</h4>

## Sobre a aplicação

Este projeto é minha reimplementação da passagem para frente e para trás do GPT-2, escrita em C11 e utilizando apenas a biblioteca padrão C POSIX como dependência. O objetivo principal desta iniciativa foi explorar detalhadamente os aspectos de baixo nível dos modelos transformadores, permitindo-me entender melhor suas operações internas, como cálculos de atenção, manipulação de tensores e aprendizado profundo. É importante destacar que o código foi desenvolvido para fins educacionais e de pesquisa, e não está pronto para ser utilizado em produção.

A lógica e os fundamentos teóricos estão documentados em notes.pdf, que descreve as etapas, os cálculos e as simplificações aplicadas ao longo do desenvolvimento. Para compilar e executar a implementação, utilize o script build.sh, que foi projetado para facilitar o processo de configuração e compilação do código em diferentes sistemas.

Adicionalmente, criei uma implementação de referência em Python, disponível no arquivo ref.py, que serviu como base para validar os resultados obtidos na versão em C. Esta implementação foi cuidadosamente testada contra o projeto nanoGPT, de Andrej Karpathy, para garantir consistência e precisão nos cálculos.

Para executar este projeto, é necessário ter um arquivo model.safetensors no diretório assets. Este arquivo contém os pesos e os parâmetros do modelo GPT-2 e pode ser obtido na plataforma HuggingFace. Certifique-se de que o arquivo esteja no formato correto e seja compatível com as implementações fornecidas.

### Recursos e Estrutura do Projeto

- `notes.pdf`: Documento detalhado com as derivações matemáticas, explicações e decisões técnicas tomadas durante o desenvolvimento.

- `build.sh`: Script automatizado para compilar o código C. Certifique-se de que todas as dependências do compilador estejam instaladas antes de usá-lo.

- `ref.py`: Código de referência em Python, usado para verificar a fidelidade e a precisão da reimplementação em C.
  assets/model.safetensors: Arquivo contendo os pesos do modelo GPT-2, necessário para executar as passagens para frente e para trás.

### Pré-requisitos

- `Compilador C`: Um compilador que suporte o padrão C11. Exemplos incluem GCC e Clang.
- `Python`: Para executar e validar os resultados com a implementação de referência.
- `model.safetensors`: Este arquivo deve ser obtido na HuggingFace. É imprescindível que os pesos correspondam ao modelo GPT-2.

### Próximos Passos

- Embora o código atual seja funcional para demonstração e aprendizado, há oportunidades para melhorias, incluindo:

Otimização de desempenho: Tornar o código mais eficiente em termos de memória e processamento.
Adição de suporte para GPUs: Implementar operações otimizadas para execução em hardware acelerado.
Documentação aprimorada: Incluir mais exemplos e explicações detalhadas sobre as funções específicas.
Integração com outras versões de GPT: Expandir o suporte para modelos maiores ou mais recentes.
Este projeto foi um excelente exercício para aprofundar meu conhecimento em inteligência artificial e sistemas de baixo nível, e espero que sirva de inspiração para outros que desejam entender a fundo os modelos transformadores.

## Criar um ambiente virtual

- Obs. Criar um ambiente virtual é opcional, mas é uma boa prática para manter o ambiente de desenvolvimento limpo e organizado.

```bash
    # criar um ambiente virtual
    python -m venv .venv

    # ativar o ambiente virtual no linux ou macOS
    source .venv/bin/activate

    # ativar o ambiente virtual no windows
    .venv\Scripts\activate
```

## Executar o projeto

```bash
    # iniciar um projeto
    python main.py
```

## Ferramentas utilizada

```PlainText
    - pip install tiktoken
    - pip install safetensors
    - pip install numpy
    - pip install torch
```

## Fonte de pesquisa

- [GPT-2s](https://huggingface.co/openai-community/gpt2) - GPT-2s é uma reimplementação do GPT-2 em C11, com passagem para frente e para trás.

## Licença

Este projeto é licenciado sob [CC0 1.0 Universal]. Consulte o arquivo [LICENÇA](https://github.com/SilvaneiMartins/gtp-2s/blob/master/LICENSE) para obter detalhes.

## Doações

Se você achar este projeto útil e quiser apoiar seu desenvolvimento contínuo, você pode fazer uma doação via `PIX` para e-mail `silvaneimartins@hotmail.com`.

Muito ❤️ pelo apoio!

## Contato

<a href="https://github.com/SilvaneiMartins">
    <img
        style="border-radius:50%"
        src="https://github.com/SilvaneiMartins.png"
        width="100px;"
        alt="Silvanei Martins"
    />
    <br />
    <sub>
        <b>Silvanei de Almeida Martins</b>
    </sub>
</a>
     <a href="https://github.com/SilvaneiMartins" title="Silvanei martins" >
 </a>
<br />
🚀 Feito com ❤️ por Silvanei Martins
