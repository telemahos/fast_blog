// GET SAMPLE
// fetch('https://api.github.com/users')
//     .then(res => {
//         return res.json()
//     })
//     .then(data => console.log(data))
//     .catch(error => console.log('ERROR'))

// POST METHOD
fetch('https://reqres.in/api/users', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: 'Noula',

        })
    })
    .then(res => {
        return res.json()
    })
    .then(data => console.log(data))
    .catch(error => console.log('ERROR'))