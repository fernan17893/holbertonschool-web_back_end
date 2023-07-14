import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  const p = Promise.allSettled([signUpUser(firstName, lastName), uploadPhoto(fileName)]);
  return p;
}
