# Ajay Raman

Hi, My name is Ajay Raman and my favorite language is R becasue it is very efficient for econometrics!

## Example Code

```
cpi_ts <- cpi_raw %>%
  transmute(
    date = as.Date(date),
    cpi  = as.numeric(value)
  ) %>%
  arrange(date) %>%
  as_tsibble(index = date) %>%
  mutate(
    infl_yoy = (cpi / lag(cpi, 12) - 1) * 100    # year-over-year (%)
  )
```

### Code Explanation

This code seperates the date and inflation measure to prepare it for time series analysis.
You will need to have R installed to use this code. See (https://www.r-project.org/).
