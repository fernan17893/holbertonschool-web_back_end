export default function signUpUser(firstName, lastName) {
  const p = Promise.resolve({ firstName, lastName });
  return p;
}
