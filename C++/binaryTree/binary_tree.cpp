#include <iostream>
#include <queue>
using namespace std;

class Node {
    public:
    int data;
    Node* right;
    Node* left;

    Node(int d) {
        data = d;
        right = left = NULL;
    }
};

Node* buildTree() {
    int d;
    cin>>d;
    if(d==-1)
    return NULL;

    Node* n = new Node(d);
    n->left = buildTree();
    n->right = buildTree();
    return n;
}

void printPreorder(Node* root) {
    if(root==NULL)
    return;

    cout<<root->data<<" ";
    printPreorder(root->left);
    printPreorder(root->right);
}
void printInorder(Node* root) {
    if(root==NULL)
    return;

    printInorder(root->left);
    cout<<root->data<<" ";
    printInorder(root->right);
}
void printPostorder(Node* root) {
    if(root==NULL)
    return;

    printPostorder(root->left);
    printPostorder(root->right);
    cout<<root->data<<" ";
}

void printLevelorder(Node* root) {
    queue<Node*> q;
    q.push(root);
    q.push(NULL);

    while(!q.empty()) {
        Node* temp = q.front();

        if(temp == NULL) {
            q.pop();
            cout<<endl;

            if(!q.empty())
            q.push(NULL);
        }
        else {
            cout<<temp->data<<" ";
            q.pop();

            if(temp->left)
            q.push(temp->left);

            if(temp->right)
            q.push(temp->right);

        }
    }
    return;
}

int main() {
    Node* root = buildTree();
    printPreorder(root);
    cout<<endl;
    printInorder(root);
    cout<<endl;
    printPostorder(root);
    cout<<endl;
    printLevelorder(root);
    return 0;
}