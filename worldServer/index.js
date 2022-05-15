const express = require('express')
const app = express()
const port = 3000
const fs = require(
    'fs'
)

app.use(express.json())

app.get('/', (req, res) => {
  res.send('Hello World!')
})

app.get('/:world', (req, res, next) => {
    let jsonToFetch = 'worlds/' + req.params.world + '.json'
    let rawdata = fs.readFileSync(jsonToFetch);
    let student = JSON.parse(rawdata);
    res.send(student)
    next()
})

app.post('/:world', (req, res, next) => {
    console.log(req.body)
    let world = JSON.stringify(req.body)
    fs.writeFileSync('worlds/' + req.params.world + '.json', world)
    res.send("Saved World")  // <==== req.body will be a parsed JSON object

})

app.listen(port, () => {
  console.log(` ${port}`)
})