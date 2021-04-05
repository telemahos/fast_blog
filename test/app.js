
let token = ''
const loginBtn = document.getElementById('login-btn');
const getBtn = document.getElementById('get-btn');
const addPostBtn = document.getElementById('add-post-btn');
const readCookieBtn = document.getElementById('readCookie-btn');
const delCookieBtn = document.getElementById('delCookie-btn');
const updatePostBtn = document.getElementById('update-post-btn');
const viewPostBtn = document.getElementById('view-post-btn')

var cookieValue = "";

// ###################################################
// ALL ABOUT LOGIN
// ###################################################
// LOGIN and Cookie Creation, if nescecery
// let loginForm = document.getElementById('loginForm');
const loginData = new FormData();
const login = () => {
	// kostas@kakoulis.de
	var the_username = document.getElementById("the_username").value;
	var the_password = document.getElementById("the_password").value;
	loginData.set('username', the_username);
	loginData.set('password', the_password);
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
		document.cookie = 'fastapiuser=' + token + '; max-age=1800;';
		// reset the input fields
		document.getElementById("the_username").value = "";
		document.getElementById("the_password").value = "";
		console.log("TOKEN11: " + token);
		document.getElementById('login-btn').disabled = true;
	})
	.catch((error) => console.log(error));
};

// ###################################################
// ALL ABOUT COOKIE's
// ###################################################
// readCookie
function readCookie() {
	if (document.cookie != "") {
		console.log('readCookie: ' + document.cookie);
	}
	else {
		console.log('there is no cookie2');
	}
}
// Load the Cookie on Page Load
function loadCookie() {
	if (document.cookie != "") {
		// When cookie is available then disable Login button
		document.getElementById('login-btn').disabled = true;
		console.log('loadCookie: ' + document.cookie);
		getCookieValue();
		return document.cookie;
	}
	else {
		console.log('there is no cookie1');
	}
}

// Inject the cookie into token
function getCookieValue() {
	cookieValue = document.cookie.split('; ').find((item) => item.startsWith('fastapiuser=')).split('=')[1];
	console.log('cookieValue: ' + cookieValue);
	token = cookieValue;
}

function deleteCookie() {
	document.cookie = "fastapiuser=; expires = Thu, 01 Jan 1970 00:00:00 GMT";
	console.log('Deleted cookie: ' + document.cookie);
}


// ###################################################
// ALL ABOUT BLOG
// ###################################################
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

// Update Blog => Post
const updatePostData = () => {
	var update_post_id = document.getElementById("update_blog_id").value;
	var update_post_title = document.getElementById("update_blog_title").value;
	var update_post_body = document.getElementById("update_blog_body").value;
	axios.put(
		'http://127.0.0.1:8000/blog/' + update_post_id, 
		{
			title: update_post_title,
			body: update_post_body
		},
		{
			headers: {
				// 'Content-Type': 'application/x-www-form-urlencoded',
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${token}`
			},
		},
	)
	.then((response) => console.log(response))	
	.catch((error) => console.log(error));
};

// Get a new Blog Post
const sendBlogPostData = () => {
	var post_title = document.getElementById("the_title").value;
	var post_body = document.getElementById("the_body").value;
	axios.post(
		'http://127.0.0.1:8000/blog',
		{
			// data
			title: post_title,
			body: post_body
		},
		{
			headers: {
				'Authorization': `Bearer ${token}`,
				'Content-Type': 'application/json',
				
			},
		},
		{withCredentials: true},
	)
	.then(function (response) {
		// handle success
		console.log("New Blog Post: " + response)
	})
	.catch((error) => console.log(error));
};

// View Blog Post by ID
const viewBloPostData = () => {
	var view_post_id = document.getElementById("view_post_id").value;
	axios.get(
		'http://127.0.0.1:8000/blog/' + view_post_id,
		{
			headers: {
				'Content-Type': 'application/json',
				'Authorization': `Bearer ${token}`
				// 'Content-Type': 'application/x-www-form-urlencoded',
			},
		},
		{withCredentials: true},
	)
	.then(function (response) {
		// handle success
		console.warn("response: " + JSON.stringify(response));
		console.log("Blog Post by ID: " + JSON.stringify(response.data.title));
		console.log("Blog Post by ID: " + JSON.stringify(response.data.body));
		document.getElementById("view_post_title").innerHTML = JSON.stringify(response.data.title);
		document.getElementById("view_post_body").innerHTML = JSON.stringify(response.data.body);
	})
	.catch((error) => console.log(error));
}

// ###################################################
// ALL ABOUT 
// ###################################################


// ###################################################
// ALL ABOUT 
// ###################################################


// ###################################################
// ALL ABOUT 
// ###################################################


// ###################################################
// ALL ABOUT EventListener's
// ###################################################
loginBtn.addEventListener('click', login);
readCookieBtn.addEventListener('click', readCookie);
delCookieBtn.addEventListener('click', deleteCookie);
updatePostBtn.addEventListener('click', updatePostData);
addPostBtn.addEventListener('click', sendBlogPostData);
getBtn.addEventListener('click', getBlog);
viewPostBtn.addEventListener('click', viewBloPostData);
