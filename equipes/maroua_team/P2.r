max_houses <- function(N, B, prices) {
  prices <- sort(prices)  # Triez les prix par ordre croissant
  houses_to_buy <- 0
  total_price <- 0

  for (price in prices) {
    if (total_price + price <= B) {
      houses_to_buy <- houses_to_buy + 1
      total_price <- total_price + price
    } else {
      break
    }
  }

  return(houses_to_buy)
}

main <- function() {
  tests <- readLines("data/P2/input.txt")

  output_file <- "data/P2/output.txt"
  sink(output_file)  # Rediriger la sortie vers le fichier output.txt

  for (i in seq(1, length(tests), by=2)) {
    line <- strsplit(tests[i], " ")[[1]]
    N <- as.integer(line[1])
    B <- as.integer(line[2])

    prices <- as.integer(strsplit(tests[i + 1], " ")[[1]])
    
    result <- max_houses(N, B, prices)
    cat("Test", (i + 1) / 2, ":", result, "\n")
  }

  sink()  # Arrêter la redirection de la sortie vers le fichier
  cat("Résultats enregistrés dans le fichier output.txt.\n")
}

main()
