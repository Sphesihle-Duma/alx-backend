import redis from 'redis'
import {promisify} from 'util'

const client = redis.createClient();

//Promisify the get method of redis client
const getAsync = promisify(client.get).bind(client)

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

async function displaySchoolValue(schoolName){
  try {
    const value = await getAsync(schoolName)
    console.log(value)
  }
  catch (error){
    console.error(error)
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100')
displaySchoolValue('HolbertonSanFrancisco')
