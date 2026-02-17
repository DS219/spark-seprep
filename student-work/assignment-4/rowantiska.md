# Rowan Tiska

Hi! My name is Rowan and a current sophomore at Boston University studying Data Science and Sustainable Energy. My favorite programming language is JavaScript because I love using React.js and creating creative frontend app.

## Example code
```
export default function Home() {

  const [design, setDesign] =  React.useState(false)

  const toggleDesign = () => {
      setDesign(!design)
  }

  return (
    <div className="lg:flex block">
        <Header/>   
      <div className="lg:w-1/2">
          <ProjectsShown design={design} />
      </div>
    </div>
  );
}
```

### Code Explaination

This code is from a personal website that I made and uses React state to show and hide certain elements on the page. In this example, the design variable is passed into the Project component to give it a true or false value for it to be shown on the page or not. In order to run this code you must install React and all necessary imports/dependencies.