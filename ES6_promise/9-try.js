export default function guardrail(mathFunction) {
    let queue = ['', 'Guardrail was processed'];
    try {
      queue = [mathFunction(), 'Guardrail was processed'];
    } catch (error) {
      queue[0] = error.toString();
    }
    return queue;
  }