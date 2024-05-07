function operadores1() {
  let precoFralda = 1.1;
  let diaFralda = 4;
  let mes = 30;

  const resultado = 1.1 * 4 * 30;
  console.log(resultado);
}

//operadores1();

function operadores2() {
  let pesoUsuario = Number(prompt("Informe o seu peso"));
  let qtdAguaDia = 35;
  let qtdAguaUsuario = (pesoUsuario * 35) / 1000;
  console.log("Você deve beber " + qtdAguaUsuario + " Litros de agua por dia");
}

//operadores2();

function operadores3() {
  let salarioBrutoUsuario = Number(
    prompt("Informe seu salário bruto, Obs: use '.' ao invés de ',' ")
  );
  let descontoPrevidencia = salarioBrutoUsuario * 0.12;
  let descontoVt = descontoPrevidencia * 0.06;
  let salarioLiquidoUsuario =
    salarioBrutoUsuario - descontoPrevidencia - descontoVt;
  console.log("Seu salário líquido é de " + "R$ " + salarioLiquidoUsuario);
}

operadores3();
