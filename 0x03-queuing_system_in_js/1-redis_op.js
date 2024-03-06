import redis from 'redis'

const client = redis.createClient();

//Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection errors
client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

// Event listener for connection closing
client.on('end', () => {
  console.log('Connection closed');
});

function setNewSchool(schoolName, value){
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName){
  client.get(schoolName, (err, reply) => {
    if (err){
      console.log(err);
    }
    else {
	console.log(reply);
    }
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100')
displaySchoolValue('HolbertonSanFrancisco')
