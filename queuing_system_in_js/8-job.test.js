const createPushNotificationsJobs = (jobs, queue) => {
    if (!Array.isArray(jobs)) {
      throw Error('Jobs is not an array');
    }

    jobs.forEach((job) => {
      const newJob = queue.create('push_notification_code_3', job).save();

      try {
        newJob.on('enqueue', () => {
          console.log(`Notification job created: ${newJob.id}`);
        });

        newJob.on('complete', () => {
          console.log(`Notification job ${newJob.id} completed`);
        });

        newJob.on('failed', (errorMessage) => {
          console.log(`Notification job ${newJob.id} failed: ${errorMessage}`);
        });

        newJob.on('progress', (progress, data) => {
          console.log(`Notification job ${newJob.id} ${progress}% complete`);
        });
      } catch (err) {}
    });
  }

  module.exports = createPushNotificationsJobs;
