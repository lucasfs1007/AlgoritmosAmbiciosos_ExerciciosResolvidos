function candy(ratings) {
    const n = ratings.length;
    const candies = Array(n).fill(1);
  
    // Percorre da esquerda para a direita garantindo que crianças com classificações mais altas ganham mais doces que seus vizinhos à esquerda.
    for (let i = 1; i < n; i++) {
      if (ratings[i] > ratings[i - 1]) {
        candies[i] = candies[i - 1] + 1;
      }
    }
  
    // Percorre da direita para a esquerda garantindo que crianças com classificações mais altas ganham mais doces que seus vizinhos à direita.
    for (let i = n - 2; i >= 0; i--) {
      if (ratings[i] > ratings[i + 1]) {
        candies[i] = Math.max(candies[i], candies[i + 1] + 1);
      }
    }
  
    // Soma o total de doces distribuídos.
    return candies.reduce((total, num) => total + num, 0);
  }
  
