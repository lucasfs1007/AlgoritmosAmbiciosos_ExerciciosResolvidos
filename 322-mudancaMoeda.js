function coinChange(coins, amount) {
    // Inicializa um array para armazenar o menor número de moedas necessário para cada valor
    const dp = new Array(amount + 1).fill(Infinity);

    // 0 moedas necessárias para fazer uma quantia de 0
    dp[0] = 0;

    // Para cada valor de 1 até a quantidade desejada
    for (let i = 1; i <= amount; i++) {
        // Para cada moeda disponível
        for (let coin of coins) {
            // Se a moeda for menor ou igual ao valor atual
            if (coin <= i) {
                // Atualiza o mínimo de moedas necessário para fazer a quantia atual
                dp[i] = Math.min(dp[i], dp[i - coin] + 1);
            }
        }
    }

    // Se a quantidade desejada não puder ser alcançada
    return dp[amount] === Infinity ? -1 : dp[amount];
}

// Exemplos de uso
console.log(coinChange([1, 2, 5], 11)); // Saída: 3
console.log(coinChange([2], 3));         // Saída: -1
console.log(coinChange([1], 0));         // Saída: 0
