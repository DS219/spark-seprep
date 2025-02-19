# John Kinney

Hi, my name is Jack (John) Kinney and my favorite programing languages are Python and JavaScript. I'm dedicated to applying my skills in problem-solving, machine learning, and full-stack development to create impactful solutions which these two languages can be great for!

## Example code

```
function getRandomFact() {
  // API URL to get a random fact
  const apiUrl = 'https://uselessfacts.jsph.pl/random.json?language=en';

  fetch(apiUrl)
    .then(response => response.json())
    .then(data => {

      console.log(data.text);
    })
    .catch(error => {
      console.error('Error fetching random fact:', error);
    });
}

getRandomFact();
```

### Code explanation

This script will display one random fact each time you run it! To run from the terminal, copy the above to a `fact.js` and run it with `node fact.js`.
You need to have Node installed! See [Node install documentation](https://nodejs.org/en). 