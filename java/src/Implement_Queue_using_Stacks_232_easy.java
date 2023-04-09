import java.util.*;;

public class Implement_Queue_using_Stacks_232_easy {
    private Stack<Integer> in, out;

    public Implement_Queue_using_Stacks_232_easy() {
        this.in = new Stack<>();
        this.out = new Stack<>();
    }

    public void push(int x) {
        this.in.push(x);
    }

    public int pop() {
        if (this.out.size() == 0) {
            while (this.in.size() > 0) {
                this.out.push(this.in.pop());
            }
        }
        return this.out.pop();
    }

    public int peek() {
        if (this.out.size() == 0) {
            while (this.in.size() > 0) {
                this.out.push(this.in.pop());
            }
        }
        return this.out.peek();
    }

    public boolean empty() {
        return (this.in.size() == 0 && this.out.size() == 0);
    }
}
