import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default async function handleProfileSignup(
    firstName,
    lastName,
    fileName,
) {
    const stat = [];
    await signUpUser(firstName, lastName)
        .then(async (data) => {
            stat.push({ status: 'fulfilled', value: data });
            await uploadPhoto(fileName);
        })
        .catch((err) => {
            stat.push({ status: 'rejected', value: err.toString() });
        });
    return stat;
}
