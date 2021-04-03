
let token = ''
const postBtn = document.getElementById('post-btn');
const getBtn = document.getElementById('get-btn');
const addPostBtn = document.getElementById('add-post-btn');

// LOGIN
const loginData = new FormData();
const sendData = () => {
	formData.set('username', 'kostas@kakoulis.de');
	formData.set('password', 'abc');
	axios.post(
		'http://127.0.0.1:8000/login',
		loginData,
		{
			headers: {
				// 'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Type': 'application/json',
			},
		},
		// {withCredentials: true},
	)
	.then(function (response) {
		// handle success
		token = response.data.access_token;
		console.log("TOKEN11: " + token)
	})
	.catch((error) => console.log(error));
};

// Get Blog => Posts or the User
const getBlog = () =>   {
	axios.get(
		'http://127.0.0.1:8000/blog', {
		headers: {
			'Authorization': `Bearer ${token}`,
		},
	})
	.then((response) => console.log(response))
	.catch((error) => console.log(error));
};

// Set a Blog => Post
const sendPostData = () => {
	axios.post(
		'http://127.0.0.1:8000/blog', 
		{
			title: 'Test Title8',
			body: 'Test Body8'
		},
		{
			headers: {
				'Content-Type': 'application/x-www-form-urlencoded',
				'Authorization': `Bearer ${token}`
			},
		},
	)
	.then((response) => console.log(response))
	.catch((error) => console.log(error));
};

getBtn.addEventListener('click', getBlog)
postBtn.addEventListener('click', sendData);
addPostBtn.addEventListener('click', sendPostData);