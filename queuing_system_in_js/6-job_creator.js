const kue = require('kue')
const queue = kue.createQueue();

const job = queue.create('push_notification_code', {
    phoneNumber: '12345',
    message: 'Fern',
}).save( function(err){
    if( !err ) console.log(`Notification job created: ${job.id}` );   
});

job.on('complete', () => console.log('Notification job completed'));

job.on('failed', () => console.log('Notification job failed'));
