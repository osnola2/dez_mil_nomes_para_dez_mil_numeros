# dez mil nomes para dez mil coisas (萬物萬名)

Documento compilado com a explicação técnica, estrutura matemática do sistema Cisterciano (0 a 9.999) e gerador multilíngue dos 10.000 nomes.

---

## 1. Alfabetos, Sistemas de Escrita e o Padrão Global

### A. Diferença entre "Alfabeto" e "Sistema de Escrita"
Na linguística (grafonômica), existe uma distinção importante:
* **Alfabeto Verdadeiro:** Sistema em que vogais e consoantes possuem letras separadas e equivalentes (ex: Latino, Grego, Cirílico, Hangul, Armênio).
* **Abjad:** Sistema consonantal (ex: Árabe, Hebraico).
* **Abugida (Alfassilabário):** Caracteres baseados em consoantes com modificadores vocálicos (ex: Devanagari, Tailandês).
* **Silabário:** Símbolos que representam sílabas completas (ex: Hiragana, Katakana, Cherokee).
* **Logógrafo:** Símbolos ideográficos que representam conceitos/palavras (ex: Caracteres Chineses - Hanzi).

### B. Contagem Mundial e Padrões Internacionais
* **Línguas Faladas no Mundo:** Aprox. **7.000 línguas**.
* **ISO 15924 (Catálogo Amplo de Escritas):** Define códigos para mais de **210 sistemas de escrita** (incluindo variações históricas e em processo de padronização).
* **Padrão Unicode (Versão 17.0):** Suporta **172 sistemas de escrita** já codificados digitalmente (102 modernos e 70 antigos/extintos).

> [!NOTE]
> **Relação de Inclusão ($172 + 210 \neq 382$):**  
> Os 172 sistemas de escrita do Unicode **já estão contidos** nos 210 códigos da norma ISO 15924. A ISO é a lista mãe ampla, enquanto o Unicode é a lista das escritas já digitalizadas nos computadores.
> $$\text{ISO 15924 (210)} \supset \text{Unicode (172)}$$

---

## 2. Tradução de Numerais: Dicionário vs. Algoritmos

Representar os números de **0 a 9.999** para as 7.000 línguas do mundo geraria:
$$\text{10.000 números} \times \text{7.000 línguas} = \mathbf{70.000.000 \text{ de entradas}}$$

Em vez de criar uma tabela estática inviável de 70 milhões de linhas, os sistemas utilizam **algoritmos de gramática combinatoria**. Com poucas palavras-chave de base (unidades, dezenas, centenas e milhares), a linguagem por extenso é gerada em tempo real.

---

## 3. O Projeto: dez mil nomes para dez mil coisas (萬物萬名)

> *"O Tao gerou o Um; o Um gerou o Dois; o Dois gerou o Três; e o Três gerou os dez mil seres."* — **Tao Te Ching**

No sistema Cisterciano (0 a 9.999), existem exatamente **10.000 símbolos geométricos únicos**, cada um representando a síntese visual de um número e seu respectivo nome em dezenas de línguas e escritas humanas.

Os arquivos do projeto ([cisterciano_web.html](file:///c:/Users/User/Desktop/Python/Hangul_cisterciano/cisterciano_web.html), [refatorado_p5.js](file:///c:/Users/User/Desktop/Python/Hangul_cisterciano/refatorado_p5.js) e [cisterciano_desktop.py](file:///c:/Users/User/Desktop/Python/Hangul_cisterciano/cisterciano_desktop.py)) aplicam esses conceitos na prática.

### A. O Sistema Numérico Cisterciano (Século XIII)
Os monges cistercianos criaram uma notação onde qualquer número de **0 a 9.999** é desenhado em uma **única haste vertical central** dividida em 4 quadrantes, cada um codificado por uma cor exclusiva no projeto:

```text
        Dezenas (Verde #34d399)    │  Unidades (Ciano #38bdf8)
      ----------------------------+----------------------------
       Milhares (Púrpura #c084fc) │ Centenas (Ouro #fbbf24)
```

* **Unidades (1 a 9):** Quadrante Superior Direito — **Ciano (`#38bdf8`)**
* **Dezenas (10 a 90):** Quadrante Superior Esquerdo — **Verde Esmeralda (`#34d399`)**
* **Centenas (100 a 900):** Quadrante Inferior Direito — **Amarelo Ouro (`#fbbf24`)**
* **Milhares (1.000 a 9.000):** Quadrante Inferior Esquerdo — **Púrpura/Roxo (`#c084fc`)**
* **Haste Central:** Branco Neutro (`#f1f5f9`)

### B. Funcionamento Técnico da Aplicação

1. **Mapeamento Interativo pelo Mouse:**
   Ao mover o cursor na tela ($700 \times 700 \text{ px}$), a posição $(X, Y)$ é convertida matematicamente para um número entre $0$ e $9.999$:
   ```javascript
   let row = Math.floor(constrain(mouseY, 0, 699) / 7);
   let number = Math.floor(map(constrain(mouseX, 0, 700), 0, 700, row * 100, (row + 1) * 100));
   ```

2. **Renderização Geométrica Modular (`drawDigit`):**
   Um único helper desenha nos 4 quadrantes da haste central apenas invertendo os vetores de direção `xDir` e `yDir`:
   ```javascript
   drawDigit(ones,      x1, y1,  1,  1); // Superior Direito
   drawDigit(tens,      x1, y1, -1,  1); // Superior Esquerdo
   drawDigit(hundreds,  x2, y2,  1, -1); // Inferior Direito
   drawDigit(thousands, x2, y2, -1, -1); // Inferior Esquerdo
   ```

3. **Gerador Multilíngue por Extenso & Visualização Sincronizada:**
   * No arquivo `cisterciano_web.html`, a função `renderHUD(num)` chama geradores algorítmicos para exibir simultaneamente o número por extenso em **mais de 22 idiomas e escritas**.
   * **Posicionamento Principal:** A coluna de **Português (PT)** fica posicionada na extrema esquerda como primeira coluna do layout.
   * **Controle de Rolagem do Texto (Checkbox "Rolagem automática do texto"):**
     * **Marcado (Ativado):** As colunas realizam a rolagem vertical contínua e sincronizada para cima.
     * **Desmarcado (Desativado):** O texto permanece estático (`translateY(0)`), exibindo apenas o trecho que cabe visivelmente na tela sem animação.
