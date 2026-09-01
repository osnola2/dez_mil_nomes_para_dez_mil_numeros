// refatorado_p5.js
// Este programa gera numerais cistercianos através do movimento do mouse.
// O código foi drasticamente reduzido usando loops e operações matemáticas.

function setup() {
  createCanvas(700, 700);
}

function draw() {
  background(220);
  
  // 1. Calcula o número usando um random seed baseado na posição do mouse
  randomSeed(mouseX * width + mouseY);
  let number = Math.floor(random(10000));
  number = constrain(number, 0, 9999);
  
  // 2. Extrai os dígitos (unidade, dezena, centena, milhar)
  let ones = number % 10;
  let tens = Math.floor((number % 100) / 10);
  let hundreds = Math.floor((number % 1000) / 100);
  let thousands = Math.floor(number / 1000);
  
  // Desenha os componentes na tela
  drawTexts(number);
  drawCistercian(350, 125, 350, 575, ones, tens, hundreds, thousands);
}

function drawTexts(num) {
  strokeWeight(1);
  fill(0);
  textSize(12);
  
  // 3. Conversão binária limpa:
  // Converte para binário e preenche zeros à esquerda para ter 16 bits
  let binStr = num.toString(2).padStart(16, '0');
  
  for (let i = 0; i < 16; i++) {
    // Pega os bits da direita para a esquerda (como no seu código original)
    let bit = binStr.charAt(15 - i);
    // Adiciona o espaçamento a cada 4 bits
    let espacoExtra = Math.floor(i / 4) * 10; 
    let yPos = 260 + (i * 10) + espacoExtra;
    
    text(bit, 30, yPos);
  }
  
  // Texto Decimal
  textSize(24);
  textAlign(CENTER);
  text(num, 350, 680);
  textAlign(LEFT); // volta ao padrão
}

function drawCistercian(x1, y1, x2, y2, ones, tens, hundreds, thousands) {
  strokeWeight(12);
  stroke(0);
  strokeCap(PROJECT); // As pontas retas da linha
  
  // Haste central
  line(x1, y1, x2, y2);
  
  let w = 150; // largura do traço
  let h = 150; // altura do traço
  
  // 4. Função helper que desenha o glifo em qualquer quadrante
  // O xDir e yDir ditam a direção que a linha "cresce" a partir do ponto central.
  let drawDigit = (digit, startX, startY, xDir, yDir) => {
    let ex = startX + w * xDir; // ponta extrema X
    let ey = startY + h * yDir; // ponta extrema Y
    
    if (digit === 1) line(startX, startY, ex, startY);
    if (digit === 2) line(startX, ey, ex, ey);
    if (digit === 3) line(startX, startY, ex, ey);
    if (digit === 4) line(ex, startY, startX, ey);
    if (digit === 5) { line(startX, startY, ex, startY); line(ex, startY, startX, ey); }
    if (digit === 6) line(ex, startY, ex, ey);
    if (digit === 7) { line(startX, startY, ex, startY); line(ex, startY, ex, ey); }
    if (digit === 8) { line(ex, startY, ex, ey); line(startX, ey, ex, ey); }
    if (digit === 9) { line(startX, startY, ex, startY); line(ex, startY, ex, ey); line(startX, ey, ex, ey); }
  };
  
  // Chamamos o helper para os 4 cantos
  drawDigit(ones, x1, y1, 1, 1);         // Superior Direito
  drawDigit(tens, x1, y1, -1, 1);        // Superior Esquerdo
  drawDigit(hundreds, x2, y2, 1, -1);    // Inferior Direito
  drawDigit(thousands, x2, y2, -1, -1);  // Inferior Esquerdo
}
