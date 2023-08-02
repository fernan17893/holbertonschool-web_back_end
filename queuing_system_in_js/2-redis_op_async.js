import redis from 'redis';
import promisify from 'util';

const client = redis.createClient();

client.on("connect", () => {
    console.log("Redis client connected");
});

client.on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
    const get = promisify(client.get).bind(client);
    const valu = get(schoolName)
        console.log(valu);
    }
    

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');