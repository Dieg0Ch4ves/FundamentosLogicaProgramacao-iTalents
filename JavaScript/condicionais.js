function condicionais1() {
  let numeroUsuario = Number(prompt("Informe um numero"));
  let numeroPar = numeroUsuario % 2;
  if (numeroPar === 0) {
    console.log("O número digita é Par!");
  } else {
    console.log("O número digita é Impar!");
  }
}

// condicionais1();

function condicionais2() {
  let pesoUsuario = Number(prompt("Qual o seu peso ?"));
  if (pesoUsuario < 80) {
    console.log("Sua categoria de luta é peso médio");
  } else if (pesoUsuario < 90) {
    console.log("Sua categoria de luta é peso pesado");
  } else if (pesoUsuario > 120) {
    console.log("Vai lutar sumo então !");
  }
}

// condicionais2();

function condicionais3() {
  let qtdTapioca = Number(prompt("Quantas tapioca você pediu?"));
  let qtdAcai = Number(prompt("Quantos açai você pediu?"));
  let totalTapioca = qtdTapioca * 15;
  let totalAcai = qtdAcai * 12;
  let contaCliente = totalAcai + totalTapioca;
  if (contaCliente > 100) {
    let formaPagamento = Number(
      prompt(
        "Qual sua forma de pagamento, 1 para = pix ou dinheiro, 2 = outra forma "
      )
    );
    if (formaPagamento == 1) {
      let contaDesconto = contaCliente - contaCliente * 0.1;
      console.log("A conta com desconto ficou " + contaDesconto);
    } else if (formaPagamento == 2) {
      let contaDesconto = contaCliente - contaCliente * 0.05;
      console.log("A conta com desconto ficou " + contaDesconto);
    } else {
      console.log("Informe uma forma de pagamento válida!");
    }
  } else {
    console.log("O valor da sua conta, não possui desconto");
  }
}

// condicionais3();

function condicionais4() {
  let letraUsuario = prompt("Digite uma letra do alfabeto");
  switch (letraUsuario.toUpperCase()) {
    case "A":
      console.log("Vogal");
      break;
    case "E":
      console.log("Vogal");
      break;
    case "I":
      console.log("Vogal");
      break;
    case "O":
      console.log("Vogal");
      break;
    case "U":
      console.log("Vogal");
      break;
    default:
      console.log("Consoante");
      break;
  }
}

// condicionais4();
