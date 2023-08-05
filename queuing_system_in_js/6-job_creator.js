import { createQueue } from "kue";

const queue = createQueue();
const jobData = {
  phoneNumber: "8675309",
  message: "This is jenny's number",
};
const job = queue.create('push_notification_code', jobData).save()

job.on('enqueue', () => {
  console.log(`Notificcation job created: ${job.id}`)
});

job.on('complete', () => {
  console.log('Notifiction job completed')
});

job.on('failed', (err) => {
  console.log('Notification job failed')
})
