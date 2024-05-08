count_peaks <- function(altitudes) {
  peaks <- 0
  n <- length(altitudes)
  
  if (n <= 2) {
    return(peaks)
  }
  
  for (i in 2:(n - 1)) {
    if (altitudes[i] > altitudes[i - 1] && altitudes[i] > altitudes[i + 1]) {
      peaks <- peaks + 1
    }
  }
  
  return(peaks)
}

main <- function() {
  tests <- readLines("../../P1/input.txt")
  
  output_file <- "../../P1/output.txt"
  sink(output_file)  # Rediriger la sortie vers le fichier output.txt
  
  for (i in 1:length(tests)) {
    test_data <- as.numeric(strsplit(tests[i], " ")[[1]][-1])
    peaks <- count_peaks(test_data)
    cat("Test", i, ":", peaks, "\n")
  }
  
  sink()  # Arrêter la redirection de la sortie
  cat("Résultats enregistrés dans le fichier output.txt.\n")
}

main()
