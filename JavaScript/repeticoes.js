function repeticoes1() {
  let listaJogadores = [];
  for (index = 6; listaJogadores.length < index; ) {
    let jogador = {
      nome: prompt("Insira o nome do jogador."),
      idade: Number(prompt("Insira a idade.")),
    };
    listaJogadores.push(jogador);
  }

  listaOrdem = listaJogadores.sort((a, b) => a.idade - b.idade);
  listaOrdem.forEach((jogador) => {
    console.log(
      "Jogador com nome " +
        jogador.nome +
        " tem a idade de " +
        jogador.idade +
        " Anos"
    );
  });
}

// repeticoes1();

function repeticoes2() {
  let numeroDigitado = 1;
  while (numeroDigitado != 0) {
    console.log("Número digitado. " + numeroDigitado);
    numeroDigitado = Number(prompt("Digite um número."));
  }
}

// repeticoes2();

function repeticoes3() {
  let resposta = "s";
  while (resposta === "s") {
    let valorCompra = Number(prompt("Digite o valor da compra."));
    let valorDinheiro = Number(
      prompt("Digite o valor em dinheiro que você vai passar.")
    );
    do {
      let troco = valorDinheiro - valorCompra;
      console.log(
        "A compra do cliente deu R$" +
          valorCompra +
          " e valor passado foi R$" +
          valorDinheiro +
          ". O troco foi de R$" +
          troco
      );
    } while (valorCompra >= valorDinheiro);

    resposta = prompt(
      "Você ira atender outro cliente? 's' para Sim e 'n' para Não "
    );
  }
}

repeticoes3();
